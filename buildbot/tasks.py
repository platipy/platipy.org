from celery import Celery
import envoy

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def update(ref):
	branch = None
	if ref == 'refs/heads/master':
		branch = 'master'
	if ref == 'refs/heads/dev':
		branch = 'dev'
	if branch is None:
		return

	envoy.run("./update.sh %s" % branch)
