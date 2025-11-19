# Dockerfile para o Cliente (requisições curl em loop)
FROM alpine/curl

# Script que roda curl em loop
CMD while true; do \
    curl -s http://server:8080; \
    sleep 5; \
done
