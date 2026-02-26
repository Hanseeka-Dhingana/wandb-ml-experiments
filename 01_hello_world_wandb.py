import wandb
import time

# 1. Initialize W&B run
wandb.init(
    project="wandb-hello-world",
    name="hello-world-run2"
)

# 2. Log a simple message as config
wandb.config.update({
    "message": "Hello, Weights & Biases!",
    "version": 1
})

# 3. Log some dummy metrics
for step in range(5):
    wandb.log({
        "step": step,
        "value": step * 3
    })
    time.sleep(1)  # Simulate time-consuming work
    
    
# 4. Finish the run
wandb.finish()

print("Hello World experiment logged to W&B!")