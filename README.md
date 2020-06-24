# Image Cryptography Based on Rubix's Cube Principle

Implementation of image encryption and decryption using Rubix's Cube Principle. This algorithm is based on 
the paper which can be found at https://www.hindawi.com/journals/jece/2012/173931/

## Prerequisites

You need to have Python2 on your system. Follow instructions at https://www.python.org/downloads/  
You also need to install numpy and Image libraries.

On Ubuntu
```
sudo apt-get install python-numpy
sudo apt-get install python-imaging
```

## Running 

1. To encrypt an image, first place that image in the ```input/``` folder  
2. Then run  
``` python encrypt.py <image_name> ```  
The encrypted image can be found at the ```encrypted_images/``` folder.       
The keys generated during encryption is stored in the ```keys.txt``` file.  
(Note: The number of iterations of encryption to be performed can be adjusted by changing the ```ITER_MAX``` value in the ```encrypt.py``` file. Larger values will make encryption more secure but it is more time consuming)

3. To decrypt the image, run  
``` python decrypt.py <image_name> ```  
And Then enter the value of the Keys (Kr, Kc and ITER_MAX)  
The decrypted image can be found at the ```decrypted_images/``` folder.     

## Example

1. To encrypt the image ```pic5.png``` stored in the ```input``` folder

![](https://github.com/jaiskid/Image-cryptography/blob/master/input/pic5.png)

Run
``` python encrypt.py pic5.png ```  

The encrypted Picture can be found at ```encrypted_images/pic5.png```

![](https://github.com/jaiskid/Image-cryptography/blob/master/encrypted_images/pic5.png)

The keys are stored in ```keys.txt ```

2. To decrypt the image
https://github.com/jaiskid/Image-cryptography/blob/master/input/pic5.png
Run
``` python decrypt.py pic5.png ``` 

and enter the key values (Kr, Kc and ITER_MAX)  

The decrypted Picture can be found at ```decrypted_images/pic3.png```

![](https://github.com/jaiskid/Image-cryptography/blob/master/decrypted_images/pic5.png)

## Text Encryption
The above project saves the Unlock key of Images which is in readable format to Encrypt the text file.
Run
``` python texten.py ```

This will encrypt the text file into keys.txt.aes.
In order to decrypt the keys.txt.aes file 
Run
``` python textdec.py ```

This will decrypt the file in the readable format

## Dependencies Modules
``` pip install Image ```

``` pip install PIL ```

``` pip install pyAesCrypt ```
