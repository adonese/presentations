FROM golang:latest

WORKDIR /app
COPY . /app
RUN go mod download
# download present package
RUN go install golang.org/x/tools/cmd/present@latest
ENV PATH="/go/bin:${PATH}"
CMD [ "present -notes" ]
EXPOSE 3999