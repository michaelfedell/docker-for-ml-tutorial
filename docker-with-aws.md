# Running Docker with AWS Credentials

Docker containers are isolated from your host machine and do not share any of the files, programs, or environment variables unless you explicitly pass them in. This means that by default, a Docker container running on your laptop will not have any AWS credentials to run commands against your account.

In production, you do not usually need to explicitly pass credentials into a Docker container; the orchestration tool will likely take care of that (AWS ECS, EKS, etc.). However, you usually will need to pass in credentials when running the container locally to develop and test.

There are a few ways to pass your credentials into a Docker container when running it. One is to pass in environment variables with the `-e` or `--env` option. This will allow you to set or pass-through environment variables from your host's shell session. Another easy way is to just mount your entire `~/.aws` folder which contains your credentials and config for the aws cli. An example command below shows this approach.

```shell
docker run -it -v ~/.aws:/root/.aws amazon/aws-cli --profile personal-sso-admin s3 ls
```
