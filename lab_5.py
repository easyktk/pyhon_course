import numpy as np
from keras import models
from keras import layers
from tensorflow.keras.datasets import mnist
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images.shape, test_images.shape, len(train_labels), len(test_labels)

#
# digit = train_images[0]
# plt.imshow(digit, cmap=plt.cm.binary)
# plt.show()

network = models.Sequential()
network.add(layers.Flatten(input_shape=(28 * 28,))) # Додано Flatten шар
network.add(layers.Dense(32, activation='relu'))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

epch = 5
history = network.fit(train_images, train_labels, epochs=epch,
batch_size=32, validation_data=(test_images, test_labels))

# plt.plot(history.history['accuracy'], label='accuracy')
# plt.plot(history.history['val_accuracy'], label='val_accuracy')
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(loc='upper left')
# plt.show()

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_loss:', test_loss, 'test_acc:', test_acc)

network.summary()

#y_pred = network.predict(train_images)

img=mpimg.imread('6.png')
# imgplot = plt.imshow(img)
# plt.show()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(gray_img, (28, 28))
_, black_white_img = cv2.threshold(resized_img, 128, 255,
cv2.THRESH_BINARY )

plt.imshow(resized_img)
plt.show()
# cv2.imshow('Raw Image', black_white_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#changed black_wite to resized
images = resized_img.reshape((1, 28 * 28))
images = images.astype('float64')/255
images.shape

y_pred_some_digit = network.predict(images)
print(y_pred_some_digit)
pred_result = np.argmax(y_pred_some_digit, axis=1)
print(pred_result)