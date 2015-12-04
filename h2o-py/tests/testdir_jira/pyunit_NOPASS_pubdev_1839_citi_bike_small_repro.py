from tests import pyunit_utils
import sys
sys.path.insert(1, "../../")
import h2o

def pubdev_1839():

    train = h2o.import_frame(pyunit_utils.locate("smalldata/jira/pubdev_1839_repro_train.csv"))

    test  = h2o.import_frame(pyunit_utils.locate("smalldata/jira/pubdev_1839_repro_test.csv"))


    glm0 = h2o.glm(x           =train.drop("bikes"),
                   y           =train     ["bikes"],
                   validation_x=test .drop("bikes"),
                   validation_y=test      ["bikes"],
                   Lambda=[1e-5],
                   family="poisson")

if __name__ == "__main__":
	pyunit_utils.standalone_test(pubdev_1839)
else:
	pubdev_1839()
