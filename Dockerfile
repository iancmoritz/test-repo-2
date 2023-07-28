FROM quay.io/astronomer/astro-runtime:8.8.0

# install the package in editable mode
RUN pip install "${AIRFLOW_HOME}/include/astronomerregistry"