# PharmaPills
PharmaPills include two software packages: PharmaVision and Pill-ID. The user interface is run on Flask, and the models are developed in Tensorflow on Kaggle notebooks.

## PharmaVision
Trained to detect misplaced drugs for automatic pharmaceutical filling stations. It can flag an error in a batch of drugs, and it can significantly reduce errors in prescription filling. Dataset was developed from NIH PillBox with transformations, creating the new PillError Dataset found in: link. Classifer model achieved 94.889% validation accuracy and 97.45% training accuracy on 10,000 images split 70-30 train-valid.
    
## PillID
Trained to identify different medications from images. We trained the model so that it can recognize the same drug from different manufacturers. This software can be used to quickly identify drugs accurately even between different manufacturers. Dataset was developed by taking images from Drugs.com, and applied transforms to increase data size. Classifer model achieved 100.0% validation accuracy and 98.7% training accuracy on 10,000 images split 70-30 train-valid.

## Developers
Dom Huh, Joytsana Sangroula, Ji Kuo
