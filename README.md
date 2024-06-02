# medium_01_celery_example

There are two possible modes to use the project

Demo mode and Development mode

## Demo mode
For testing hypothesis

### run project
    make docker-up-all
### create demo task
    make task-create
### check task status
    make task-check
### stop project
    make docker-down

## Development mode
For development

### install project
    make install
### setup environment
    make docker-up
### run django
    make run
### run celery worker
    make celery-worker
### stop environment
    make docker-down