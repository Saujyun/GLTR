from utils import init_logger
step_size = 120
batch_size = 5
frames = 16

if __name__ == '__main__':
    logger =  init_logger("train_log","test")
    logger.info("batch_size="+str(batch_size))
    logger.info("step_size="+str(step_size))
    logger.info("frames="+str(frames))