# PNEUNOMIA-DETECTION-USING-CNN


An automated system using machine learning techniques to accurately and efficiently detect pneumonia and other lung diseases(Tuberculosiand Covid-19) from chest X-ray images, enabling faster and more reliable
diagnoses for timely medical intervention.

# METHODOLOGY
- Gather lung disease datasets and select the best available dataset for
  each class.
- The images of the gathered dataset are preprocessed, rescaled, and
  augmented as a part of preprocessing.
- The system is trained using the newly compiled dataset of labeled
  chest X-ray images, where each image is annotated into pneumonia,
  normal, tuberculosis, or COVID-19.
- Adjustments are made to the model based on the analysis
  post-training
- After training, a CXR image image is fed into the network to
  generate a prediction indicating the likelihood of lung disease.
# RESULTS
- After training the model for 100 epochs, the model achieved a
  training loss of 0.0641 and a training accuracy of 0.01706 percent.
- The validation loss at the end of the training was 0.1224, with a
  validation accuracy of 99.517percentage
- After evaluating the model on the test dataset, it achieved a test loss
  of 0.0241 and test accuracy of 99.356 percentage
  

  
**1.** Model of Jv2.13 [99.27_ acc] Dataset 5.1.1, Arch 1, 100 epoch, 16 batch size.h5:
         [https://drive.google.com/file/d/1ibOHcW0NQxFlDT_ghPf9HGKqZ6o0Lq6f/view?usp=sharing](https://drive.google.com/file/d/1HFbNxA7ZdgT9T7aGwGGmJKMDhjnF7B6o/view?usp=sharing)
