from contextlib import contextmanager
from logging import getLogger

import celery.app.task
from django.db.transaction import get_connection
from kombu.exceptions import OperationalError as KombuOperationalError
from kombu.transport.pyamqp import Transport as PyamqpTransport

from .exception import CeleryTaskApplyException

logger = getLogger(__name__)

__all__ = ["PatchedTask"]

transport_errors = (
        (KombuOperationalError,)
        + PyamqpTransport.connection_errors
        + PyamqpTransport.channel_errors
)


class PatchedTask(celery.app.task.Task):
    try_apply_async = True  # wrap to try_except by default behaviour
    propagate_exception = True  # propagate exception by default

    @contextmanager
    def wrap_connection_exceptions(self):
        connection_succeed = True
        try:
            yield
        except transport_errors as exc:
            connection_succeed = False
            raise exc
        finally:
            logger.debug("celery.task.connection.succeed | ", connection_succeed)

    @contextmanager
    def wrap_apply_async_exceptions(self):
        apply_succeed = True
        try:
            with self.wrap_connection_exceptions():
                yield
        except Exception as e:
            apply_succeed = False
            logger.error("celery.task.apply_async.failed | %s", self.name)
            if self.propagate_exception:
                raise CeleryTaskApplyException(e)
        finally:
            logger.debug("celery.task.apply_succeed | %s", apply_succeed)

    def apply_async(
            self,
            args=None,
            kwargs=None,
            task_id=None,
            producer=None,
            link=None,
            link_error=None,
            shadow=None,
            **options,
    ):
        if get_connection().in_atomic_block:
            logger.warning("celery.task.apply_async.in_atomic_block | %s", self.name)

        if not self.try_apply_async:
            return super().apply_async(
                args, kwargs, task_id, producer, link, link_error, shadow, **options
            )

        with self.wrap_apply_async_exceptions():
            return super().apply_async(
                args, kwargs, task_id, producer, link, link_error, shadow, **options
            )
