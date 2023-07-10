FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task

COPY . ./

RUN pip install -r requirements.txt

# You can overwrite command in `serverless.yml` template
CMD ["app.handler"]
