# 2022-02-08T16:06:31.483687
import vitisng

client = vitisng.create_client()
client.set_workspace(path="/proj/xirsqa/impflow/austino/2022.1/workspaces/git_source_control_example")

app = client.create_app(name="concurrent_kernel_execution", platform="/proj/xbuilds/2022.1_daily_latest/internal_platforms/xilinx_aws-vu9p-f1_shell-v04261818_201920_3/xilinx_aws-vu9p-f1_shell-v04261818_201920_3.xpfm", template="vitis_examples/host/concurrent_kernel_execution")

