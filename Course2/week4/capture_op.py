
import subprocess

result = subprocess.run(["host","8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout) # result has a b -> means an array of bytes

# Data in computers is stored and transmitted in bytes and each can represent up to 256 characters. But there are thousands of possible characters out there used to write in various languages. Chinese, for example, requires over 10,000 different characters. To be able to write in those languages, several specifications called encodings have been created over time to indicate which sequences of bytes represent which characters. Nowadays, most people use UTF-8 encoding, which is part of the Unicode standard that lists all the possible characters that can be represented. So going back to our example when we execute the command using run, Python doesn't know which encoding to use to process the output of the command. So it simply represents it as a series of bytes. If we want this to become a proper string, we can call the decode method. This method applies an encoding to transform the bytes into a string. By default, it uses a UTF-8 encoding which is what we want. So with all that said, let's transform our array of bytes into a string and then split it into several pieces.
# Start transcript at 3 minutes 25 seconds3:25
# In this way, we're operating with the output of the command that we ran, and we can do whatever we need to do with it. For example, we can choose to keep the last element of the list, which is the name that corresponds to the IP that we're looking for. Great. So we just looked at the captured standard output. But what about standard error? If we use the capture output parameter and the command writes any output to standard error, it will be stored in the std or attribute of the completed process instance. Let's look at an example of this. We'll try executing the rm command, which we use for removing files passing a filename that doesn't exist.
# Start transcript at 4 minutes 20 seconds4:20
# Let's check the return code of the command.
# Start transcript at 4 minutes 27 seconds4:27
# Okay. It failed. Just like we expected. Now, let's check the contents of the stdout and stderr attributes.
# Start transcript at 4 minutes 43 seconds4:43
# So we see that in this case, the standard output was empty. But there was an error printed, a standard error which we can access through the stderr attribute. This is a great example of how standard output and standard error are actually different streams. So Python captures them separately. Okay. We've now seen that we can execute system commands from Python and check whether they succeeded or failed. We've also seen how to capture the standard output and standard error streams so we can use their content in our scripts. These skills can be super useful when writing scripts that your system commands for some involved task and letting our Python scripts cover a broader range of tasks. In the next video, we'll wrap up our discussion on sub-process module by learning some more advanced things that we can do when calling external commands.

print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
