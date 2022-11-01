




import numpy as np

from caffe2.python import workspace, cnn, core
from caffe2.python import timeout_guard
from caffe2.proto import caffe2_pb2


def init_model(self):
    train_model = cnn.CNNModelHelper(
        order="NCHW",
        name="resnet",
        use_cudnn=True,
        cudnn_exhaustive_search=False
    )
    self.train_model = train_model

    test_model = cnn.CNNModelHelper(
        order="NCHW",
        name="resnet_test",
        use_cudnn=True,
        cudnn_exhaustive_search=False,
        init_params=False,
    )
    self.test_model = test_model

    self.log.info("Model creation completed")


def fun_per_epoch_b4RunNet(self, epoch):
    pass


def fun_per_iter_b4RunNet(self, epoch, epoch_iter):

    learning_rate = 0.05
    for idx in range(self.opts['distributed']['first_xpu_id'],
                     self.opts['distributed']['first_xpu_id'] +
                     self.opts['distributed']['num_xpus']):
        caffe2_pb2_device = caffe2_pb2.CUDA if \
            self.opts['distributed']['device'] == 'gpu' else \
            caffe2_pb2.CPU
        with core.DeviceScope(core.DeviceOption(caffe2_pb2_device, idx)):
            workspace.FeedBlob(
                '{}_{}/lr'.format(self.opts['distributed']['device'], idx),
                np.array(learning_rate, dtype=np.float32)
            )


def run_training_net(self):
    timeout = 2000.0
    with timeout_guard.CompleteInTimeOrDie(timeout):
        workspace.RunNet(self.train_model.net.Proto().name)
