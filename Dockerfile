FROM python:3.12-alpine AS base

ARG ENVIRONMENT

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN PIP_USER=1 pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN if [ "$ENVIRONMENT" = "test" ]; then PIP_USER=1 pipenv install --system --deploy --ignore-pipfile --dev; else PIP_USER=1 pipenv install --system --deploy --ignore-pipfile; fi


FROM python:3.12-alpine

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
COPY --chown=myapp:user --from=base ${PYROOT}/ ${PYROOT}/

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/

COPY --chown=myapp:user app ./app
USER 1234

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]