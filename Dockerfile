FROM golang:latest

WORKDIR /app
COPY . /app
RUN go mod download
# download present package
RUN go install golang.org/x/tools/cmd/present@latest

CMD [ "/go/bin/present -notes" ]
EXPOSE 3999