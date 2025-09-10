FROM alpine:latest

# Create non-root user and group with UID/GID 1001
RUN addgroup -g 1001 -S appuser && adduser -u 1001 -S -G appuser appuser

# App dir with proper ownership
WORKDIR /app
RUN chown -R 1001:1001 /app

# Drop privileges
USER 1001:1001

# Example command (replace with your app)
CMD ["sh", "-c", "id && whoami && echo 'running as non-root'"]
