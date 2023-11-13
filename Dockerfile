FROM postgis/postgis

ENV POSTGRES_DB=sseguro
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=ruteo

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-13-pgrouting \
    && rm -rf /var/lib/apt/lists/*

# COPY ./my-postgres.conf /etc/postgresql/postgresql.conf

EXPOSE 5432

CMD ["postgres"]