# medium_01_celery_example

There are two possible modes to use the project

Demo mode and Development mode

## Demo mode
For testing hypothesis

### run project
    make docker-up-all
#### Positive scenario
    make call-task-simple
    # > 200
    make call-task-wrapped
    # > 200
#### Negative scenario
    # switch Off rabbitMQ
    make disaster
    #
    make call-task-simple
    # > 500
    make call-task-wrapped
    # > 200
    #
    # switch On rabbitMQ
    make heal

### Check task result
    make check-task id=<task_id>

### stop project
    make docker-down

## Development mode
For development

### install project
    make install
### setup environment
    make docker-up
    make migrate
    make initadmin
### run project
    make run
    make celery-worker
### stop environment
    make docker-down