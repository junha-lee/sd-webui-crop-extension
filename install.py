import launch
# launch is imported in context of webui
if not launch.is_installed("dghs-imgutils") and not launch.is_installed("dghs-imgutils[gpu]"):
    import torch.cuda as cuda
    print("Installing dghs-imgutils")
    launch.run_pip("install dghs-imgutils[gpu]" if cuda.is_available() else "install dghs-imgutils")