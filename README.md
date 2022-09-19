
# Flask App on Fly.io

```
A template for who want to deploy flask app on fly.io
```

Both using docker when deploy to fly.io, 
`flask_min` is handled by fly.io, 
`flask_min_custom_docker` is a simple template for trying to make custom image.

- flask_min
```bash
# Check fly.toml to see detail.
# builder = "paketobuildpacks/builder:base"
- Type on fly.io: python app
- Python: 3.10.7 (fly.io default)
```

- flask_min_custom_docker
```bash
- Type on fly.io: docker app
- Python: 3.9
```
