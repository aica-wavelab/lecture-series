---
layout: default
title: 2. Mapping by demonstration
nav_order: 5
parent: Tutorials
---

# Mapping by demonstration
{: .no_toc}

A computer program is a sequence instructions for a computer to execute. Programs often take inputs, process them, and produce outputs. The way inputs are processed are usually explicited by the human programmer, using a programming language.
Machine learning (ML) offers an alternative to explicit programmation: ML algorithms can learn to process data from examples. The human developper provides pairs of input and its corresponding output, and the ML model is then optimized to reproduce the mapping from the example provided.
We call this approach **mapping by demonstration**, and finds many applications in the creative and cultural industries: in performing arts (gesture to sound), in video games, in robotics, among others.

This chapter will teach you how to build a real-time mapping from gesture to sound using ML and [Pure Data](https://puredata.info/) (Pd), a free an open-source **visual programming language** for creating interactive computer music and multimedia works. In particular, this chapter will teach you how to use your smartphone as a gesture sensor device, build a minimal sound synthesizer in Pd, and train a ML model to **control the synthesizer from gestures you choose!**

Second, you will learn how to do the same using the Wekinator, a free, open source software that allows anyone to use machine learning to map arbitrary OSC messages.

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Use your phone as a sensor device

Smartphones are excellent sensor devices because they include a large array of built-in sensors. For motion, they are equipped with accelerometers, gyroscopes, and step detection sensors. For geolocalisation, they are equipped with geopositioning, magnetic field detection, and light sensors. For touch detection, most touch screen enable precise multi-finger detection.

Additionally, smartphones are widely accessible and come with the advantage of wireless connectivity, allowing for seamless data transmission without the need for physical cables. Their portability ensures they can be used in various settings, especially in performance-based contexts where mobility is essential. Moreover, smartphones have significant computing power, enabling them to not only collect but also process complex data in real-time.

Open Sound Control (OSC) serves as an effective way to stream this sensor data. OSC is a communication protocol initially designed for networking sound synthesizers, computers, and other multimedia devices, offering more flexibility and a higher level of organization than traditional MIDI protocols. OSC signals can carry a variety of data types and are sent over standard network protocols like UDP or TCP. This compatibility with modern networking technologies makes OSC an ideal choice for transmitting the rich sensor data collected by smartphones. In creative and technical applications, OSC allows for this data to be streamed in real-time, enabling dynamic and interactive experiences.

An Open Sound Control (OSC) message is structured to include an address pattern followed by typed arguments. Here's a simple example of an OSC message:

- Address Pattern: /filter/frequency
- Arguments: 440.0

In this example, /filter/frequency is the address pattern that indicates where the message is destined within the OSC namespace. It's akin to a URL path in web development, pointing to a specific function or parameter in the receiving device or software.

The argument 440.0 is the value that is being sent to the specified address. In this context, it could represent a frequency value in Hertz that is being sent to a sound synthesizer's filter frequency parameter.

The OSC message is compact and efficient, capable of supporting multiple arguments of different types (like integers, floats, strings, etc.) following the address pattern. 


### Send OSC messages from your phone

Free mobile applications exist to stream sensor data from your phone. We recommend:

- [Sensors2OCS](https://sensors2.org/osc/) (Android) allowing to stream all the sensors of your phone as OSC messages
- [Osc controller](https://play.google.com/store/apps/details?id=com.ffsmultimedia.osccontroller&hl=de) (Android) that proposes generic button and slider interfaces to send OSC messages

To send OSC messages from your phone to your computer, you need to connect your phone and your computer to the same network. You can either use a local network (wifi) or a global network (internet). In both cases, you need to know the IP address of your computer. You can find it by typing `ipconfig` in the terminal (MacOS) or `ipconfig` in the command prompt (Windows), or in the network settings of your computer.

Both application should be configurated with the IP address of your computer and the port number to send OSC messages to. The port number is a number between 0 and 65535. We recommend to use a number between 8000 and 9000.

### Receive OSC messages on your computer in Pure Data

[Pure Data](https://puredata.info/) is a free and open-source visual programming language for creating interactive computer music and multimedia works. Pd enables musicians, visual artists, performers, researchers, and developers to create software graphically, without writing lines of code. Pd is used to process and generate sound, video, 2D/3D graphics, and interface sensors, input devices, and MIDI. Pd can easily run on micro-computers such as Raspberry Py and is hence a great tool for prototyping interactive systems.
We recommend using the [Plug Data](https://plugdata.org/) version of Pd, as it provides a more user-friendly interface, and can be used as a standalone app or as a VST3, LV2, CLAP or AU plugin.

You can download below a Pd patch we wrote to receive OSC messages from your phone. You can open it with Plug Data.

[2a_phone_sensors.pd](https://github.com/aica-wavelab/aica-project-workshop/tree/main/2_mapping_demonstration){: .btn target="_blank"}

![2a_phone_sensors](/assets/images/tutorials/2a_phone_sensors.png)

Let's go through the patch.
The `loadband` object send a `bang` message (trigger signal) when the Pd patch is loaded. It is generally used to initialize settings.
The `listen 8000` object is a message triggered by the `loadbang`. It indicates that the program will listen for incoming OSC messages on port 8000. `netreceive -u -b` is configured to receive network messages using UDP protocol (-u for UDP and -b for binding to a port, which is set at 8000 from the previous object). Hence, the `netreceive` object will receive all raw messages, including those formatted in OSC, sent to port 8000.
`oscparse` takes the raw OSC messages received from netreceive and parses them into a format that can be understood and used in Pd. Note that `oscparse` belongs to an external library named `osc` that you can install with the external manager named `deken`. The deken is a repository of all available external developed for Pd, and allow you to quickly install their last version from within Pd.
 You can access it from the menu `Settings/Externals`. Search for `osc` and install the library.

![deken](/assets/images/tutorials/deken.png)

At this stage, you should be able to receive OSC messages from your phone in Pd. You can also use the `print` object to display incomming messages in the console and check that you received the formatted OSC messages correctly.

The rest is just a matter of extracting the information you need from the OSC messages: route the numerical values (arguments) from their address pattern, process, and scale the numerical values to fit your needs. The two applications might have a different OSC message format (might add a keyword in the address pattern, or send the values in a different order), so you might need to adapt the patch to your needs.

## Build a minimal sound synthesizer

Now we can stream sensor data from our phone to Pd, we can for exemple track and record motion gestures.
Let's now build a sound synthesizer that we will control from the gestures.

[2b_sound_synthesis.pd](https://github.com/aica-wavelab/aica-project-workshop/tree/main/2_mapping_demonstration){: .btn target="_blank"}


![2b_sound_synthesis](/assets/images/tutorials/2b_sound_synthesis.png)

Many techniques exist to synthesize sound. In this example, we will use substractive synthesis. The principle is to start from a complex sound (e.g., white noise) and remove some of its harmonics using a filter, in order to obtain a simpler sound.

The `noise~` object generates white noise. The `~` indicates that the object is a signal object (rather than a message), i.e., it processes audio signals. 
The `vcf~` object is a voltage-controlled filter. It takes the white noise as input and two filter paramters:

1. The cut-off frequency (in Hz) , which is the frequency above which the harmonics are removed.
2. The Q factor, which is the resonance of the filter. The higher the Q factor, the more the harmonics are removed.

Both parameters are controled using horizontal sliders. 

> {: .warning }
> Be sure to turn the volume of your computer down before playing with the sliders, as the sound can be very loud!

The output of the filter is sent to the `dac~` object, which is the digital-to-analog converter that converts the digital signal into an analog signal that can be played by your speakers. You can activate the DSP (digital signal processing) by clicking on the `⏼` button on the bottom right corner of your screen.

## Map sensors to synthesis parameters with ml-lib in Pure Data

At this stage, we successfully received OSC messages from a smartphone and created a simple sound synthesizer controlled by two parameters (cut-off frequency and Q value).
However, we still do not have a mapping between the OSC messages and the synthesis parameters and programming such a mapping by hand can be tedious and time-consuming. We will now use machine learning to learn this mapping from examples.

You can download below the Pd patch to train a ML model to map OSC messages to the cut-off frequency and Q value of the filter.

[2c_ml_regression_mapping.pd](https://github.com/aica-wavelab/aica-project-workshop/tree/main/2_mapping_demonstration){: .btn target="_blank"}

![2c_ml_regression_mapping](/assets/images/tutorials/2c_ml_regression_mapping.png)

This patch require to install the ml-lib library. Unfortunately, this library is not up-to-date in the Deken, so you will have to install it manually. You can find the latest releases of the library at this address:

[ml-lib](https://github.com/irllabs/ml-lib/releases){: .btn target="_blank"}

Once downloaded, copy paste the folter `ml.lib` in the folder `Library/plugdata/Library/Extra` (MacOS) or `PlugData/extra` (Windows) and reboot Plug Data.

You should now be able to load various machine learning classifier or regressor. We will use the `ml.ann` which is a generalist artificial neural network.

First, we must conduct data collection, e.g, gathering input (gesture data) and their corresponding outputs (synthesizer parameters).
Open both patches `2a_phone_sensors.pd`, `2b_sound_synthesis.pd`, and check that your patch `2c_ml_regression_mapping.pd` receive the signals from both the phone and the synthesizer. 

Then, click on the radio button and select the middle one (data collection). This will start the recording of the data in the `ml.ann` object. You can record as many examples as you want, while changing the position of the phone, and the values of the sound synthesizer.

When you are done, click on the `train` message to start training your artificial neural network. 
Check the console to see if there's any error messages.

Once the model is trained, click on the third mode (right button) to start the prediction. You should now be able to control the sound synthesizer from the OSC messages sent by your phone.

## Map sensors to synthesis parameters with Wekinator

The Wekinator is a free and standalone software that allows to do the exact same steps as in the patch `2c_ml_regression_mapping.pd` but in a more user-friendly interface. The wekinator accept and send arbitrary OSC messages.

You can download the Wekinator at this address:

[Wekinator](http://www.wekinator.org/){: .btn target="_blank"}

Try to train a new mapping using the Wekinator and the `2a_phone_sensors.pd` and `2b_sound_synthesis.pd` patches.

Dr. Benedikt Zönnchen provided a live demonstration of the wekinator using [Processing](https://processing.org/) (input) and [SuperCollider](https://supercollider.github.io/) (output). You can find the code and the video of the demonstration at this address:

[Slides: replacing code with machine learning](https://syncandshare.lrz.de/getlink/fiByPXEJ9rS4yR42qToaSr/presentations_aica_2023.zip){: .btn target="_blank"}
[Code: replacing code with machine learning](https://syncandshare.lrz.de/getlink/fiSxeku21dD6oZ2WZagVKW/){: .btn target="_blank"}