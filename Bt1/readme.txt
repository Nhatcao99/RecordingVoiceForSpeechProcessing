
Tutorial:
Concept:
Begin the software by open on command line with an argument(a txt file with the paper's information), example on macOS/Ubuntu command line:

python homework1.py doisong.txt

homework1.py is file name
Doisong.txt is parsing argument(make sure the file exist)

The program will divide the text file to sentences and store it in an array


NOTE:during recording , every time you save a wave file , its name and the text in it will be appended to an output.txt. But if you choose to delete that file and re-record it (read the steps below), you must delete the appended lines in the file manually. 

Usage:
Button number1: Start Recording 
The array will pass each sentence continuously every time you click this button
Also at this point you are good to record

Button number2: Save Record
The button will make program stop the ongoing record and save it to a wav file
(These file are named continuously "sentence1.wav", "sentence2.wav",...)
If it is the last sentence , program will save and automatically shut down

If no recording happening upon clicking the button, program return "no ongoing record"


Button number3: Delete Previous Record
If you are recording something and fail, you save the file and use this button
It will delete the file you have save and you are good to record the senesce again

Button number4: Stop recording
Shutdown everything (not recommended using upon finishing all the work)

