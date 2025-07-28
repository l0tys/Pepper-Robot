# **Code to control Pepper Robot**

Code for SoftBank Robotics humanoid robot Pepper using NAOqi SDK with Python 2.7.17

Since most if not all available software options are deprecated and/or are removed from the internet for Pepper 2.5 the only option is to use a community based version on GitHub of NAOqi SDK which only supports Python 2.7

```py
https://github.com/AnonKour/pynaoqi
```

---

## Factory reset Pepper

To factory reset connect to it using SSH to open the boot-config configuration page, Pepper's username usually is nao

```py
ssh nao@[Pepper's IP]
```

Then input the following command to open the boot-config configuration

```py
qicli call ALAutonomousLife.switchFocus ‘boot-config/.’
```

When the boot-config configuration page opens select 'Option', and click 'factory reset'