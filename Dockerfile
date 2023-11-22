FROM golang:latest

WORKDIR /app
COPY . /app
RUN go mod download
# download present package
RUN go install golang.org/x/tools/cmd/present@latest
ENV PATH="/go/bin:${PATH}"
# make present package executable
RUN chmod u+x /go/bin/present
CMD [ "/go/bin/present -notes" ]
EXPOSE 3999