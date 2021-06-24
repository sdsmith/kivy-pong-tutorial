from setuptools import setup

def get_install_requirements():
    reqs = [
        "wheel>=0.36.2",
        "kivy[base]>=2"
    ]
    return reqs

setup(
    name="kivy-pong-tutorial",
    install_requires=get_install_requirements(),
    python_requires=">=3.9",
)