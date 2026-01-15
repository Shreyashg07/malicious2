# =========================================================
# SAMPLE DOCKERFILE FOR SECURITY SCANNING / ML TRAINING
# Contains both benign behavior and synthetic threat logic
# =========================================================

FROM python:3.10-slim

# -------------------------------
# BENIGN: metadata & maintainer
# -------------------------------
LABEL maintainer="dev-team@example.com"
LABEL description="Sample application container"

# -------------------------------
# BENIGN: working directory
# -------------------------------
WORKDIR /app

# -------------------------------
# BENIGN: dependency installation
# -------------------------------
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# THREAT (synthetic): PATH hijack
# -------------------------------
# Intent: change execution order (logic-level threat)
ENV PATH="/tmp/.bin:${PATH}"

# -------------------------------
# BENIGN: application copy
# -------------------------------
COPY src/ /app/src/

# -------------------------------
# THREAT (synthetic): conditional execution via ARG
# Intent: hidden logic triggered only with build flag
# -------------------------------
ARG ENABLE_EXTRA
RUN if [ "$ENABLE_EXTRA" = "true" ]; then \
        echo "hidden_logic_marker" > /tmp/.feature_flag ; \
    fi

# -------------------------------
# BENIGN: debug logging
# -------------------------------
RUN echo "Build completed successfully"

# -------------------------------
# THREAT (synthetic): obfuscated logic chain
# Intent: logic obfuscation without external payloads
# -------------------------------
RUN true || echo "fallback_execution_path"

# -------------------------------
# BENIGN: cache cleanup
# -------------------------------
RUN rm -rf /root/.cache

# -------------------------------
# THREAT (synthetic): metadata hiding
# Intent: store hidden indicators in labels
# -------------------------------
LABEL build.note="normal"
LABEL build.extra="encoded_indicator_X9"

# -------------------------------
# BENIGN: expose service port
# -------------------------------
EXPOSE 8080

# -------------------------------
# THREAT (synthetic): CMD chaining
# Intent: post-start side effect
# -------------------------------
CMD ["sh","-c","python src/app.py && echo runtime_marker"]
