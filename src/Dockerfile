FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task

ARG DATA_PATH

COPY ./handler.py ./
COPY ./requirements.txt ./
COPY ./${DATA_PATH}training_storage/ ./training_storage/

RUN pip install -r requirements.txt

# You can overwrite command in `serverless.yml` template
CMD ["handler.ask"]
