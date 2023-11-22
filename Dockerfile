FROM golang:latest

WORKDIR /app
COPY . /app
RUN go mod download
# download present package
RUN go install golang.org/x/tools/cmd/present@latest

CMD [ "/go/bin/present", "-http", "0.0.0.0:3999" ]
EXPOSE 3999