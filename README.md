# Fastapi Skeleton

Fastapi Skeleton is a code base to start any project using Fast API


## Installation

Use Poetry to install the dependencies.

```bash
export LANG="en_US.UTF-8"
poetry shell
poetry install --no-root
```

## Usage

### Development
```bash
uvicorn src.app:fast_api --host=<APP_HOST> --port=<APP_PORT> --log-level=debug
```
1. APP_HOST: is the host that app run. Example: 0.0.0.0
2. APP_PORT: is the port that app run. Example: 8001

### Docker
#### Build Docker image
```bash
docker build -t <IMGAE_NAME> --progress=plain -f Dockerfile . &> docker_build.log
```
#### Run Docker container
```bash
docker run --network <CONTAINER NETWORK> -p <EXTERNAL_PORT>:<CONTAINER_APP_PORT>  --env-file <ENV FILE> --name <CONTAINER_NAME> -d <IMGAE_NAME>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)