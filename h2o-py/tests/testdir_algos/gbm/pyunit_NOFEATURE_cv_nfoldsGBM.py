from tests import pyunit_utils
import sys
sys.path.insert(1, "../../../")
import h2o

def cv_nfoldsGBM():
  # Connect to h2o
  h2o.init(ip,port)

  prostate = h2o.import_frame(path=pyunit_utils.locate("smalldata/logreg/prostate.csv"))

  #prostate.summary()

  prostate_gbm = h2o.gbm(y=prostate[1], x=prostate[2:9], nfolds = 5, distribution="bernoulli")
  prostate_gbm.show()
  
  # Can't specify both nfolds >= 2 and validation data at once
  try:
    h2o.gbm(y=prostate[1], x=prostate[2:9], nfolds=5, validation_y=prostate[1], validation_x=prostate[2:9], distribution="bernoulli")
    assert False, "expected an error"
  except EnvironmentError:
    assert True

if __name__ == "__main__":
	pyunit_utils.standalone_test(cv_nfoldsGBM)
else:
	cv_nfoldsGBM()
