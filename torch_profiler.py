import torch
import torchvision.models as models
from torch.profiler import profile, record_function, ProfilerActivity
model = models.resnet18()
inputs = torch.randn(5, 3, 224, 224)
with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
    with record_function("model_inference"):
        model(inputs)
print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))
print(prof.key_averages(group_by_input_shape=True).table(sort_by="cpu_time_total", row_limit=10)

if torch.cuda.is_available():
    device = 'cuda'
elif torch.xpu.is_available():
    device = 'xpu'
else:
    print('Neither CUDA nor XPU devices are available to demonstrate profiling on acceleration devices')
    import sys
    sys.exit(0)

activities = [ProfilerActivity.CPU, ProfilerActivity.CUDA, ProfilerActivity.XPU]
sort_by_keyword = device + "_time_total"

model = models.resnet18().to(device)
inputs = torch.randn(5, 3, 224, 224).to(device)

with profile(activities=activities, record_shapes=True) as prof:
    with record_function("model_inference"):
        model(inputs)

print(prof.key_averages().table(sort_by=sort_by_keyword, row_limit=10))

model = models.resnet18()
inputs = torch.randn(5, 3, 224, 224)

with profile(activities=[ProfilerActivity.CPU],
        profile_memory=True, record_shapes=True) as prof:
    model(inputs)

print(prof.key_averages().table(sort_by="self_cpu_memory_usage", row_limit=10))
from torch.profiler import schedule

my_schedule = schedule(
    skip_first=10,
    wait=5,
    warmup=1,
    active=3,
    repeat=2)

sort_by_keyword = "self_" + device + "_time_total"

def trace_handler(p):
    output = p.key_averages().table(sort_by=sort_by_keyword, row_limit=10)
    print(output)
    p.export_chrome_trace("/tmp/trace_" + str(p.step_num) + ".json")

with profile(
    activities=activities,
    schedule=torch.profiler.schedule(
        wait=1,
        warmup=1,
        active=2),
    on_trace_ready=trace_handler
) as p:
    for idx in range(8):
        model(inputs)
        p.step()

