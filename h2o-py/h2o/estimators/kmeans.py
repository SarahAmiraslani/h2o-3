#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OKMeansEstimator(H2OEstimator):
    """
    K-means

    Performs k-means clustering on an H2O dataset.
    """

    algo = "kmeans"
    supervised_learning = False

    def __init__(self,
                 model_id=None,  # type: Optional[Union[None, str, H2OEstimator]]
                 training_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 validation_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 nfolds=0,  # type: int
                 keep_cross_validation_models=True,  # type: bool
                 keep_cross_validation_predictions=False,  # type: bool
                 keep_cross_validation_fold_assignment=False,  # type: bool
                 fold_assignment="auto",  # type: Literal["auto", "random", "modulo", "stratified"]
                 fold_column=None,  # type: Optional[str]
                 ignored_columns=None,  # type: Optional[List[str]]
                 ignore_const_cols=True,  # type: bool
                 score_each_iteration=False,  # type: bool
                 k=1,  # type: int
                 estimate_k=False,  # type: bool
                 user_points=None,  # type: Optional[Union[None, str, H2OFrame]]
                 max_iterations=10,  # type: int
                 standardize=True,  # type: bool
                 seed=-1,  # type: int
                 init="furthest",  # type: Literal["random", "plus_plus", "furthest", "user"]
                 max_runtime_secs=0.0,  # type: float
                 categorical_encoding="auto",  # type: Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"]
                 export_checkpoints_dir=None,  # type: Optional[str]
                 cluster_size_constraints=None,  # type: Optional[List[int]]
                 ):
        """
        :param model_id: Destination id for this model; auto-generated if not specified.
               Defaults to ``None``.
        :type model_id: Union[None, str, H2OEstimator], optional
        :param training_frame: Id of the training data frame.
               Defaults to ``None``.
        :type training_frame: Union[None, str, H2OFrame], optional
        :param validation_frame: Id of the validation data frame.
               Defaults to ``None``.
        :type validation_frame: Union[None, str, H2OFrame], optional
        :param nfolds: Number of folds for K-fold cross-validation (0 to disable or >= 2).
               Defaults to ``0``.
        :type nfolds: int
        :param keep_cross_validation_models: Whether to keep the cross-validation models.
               Defaults to ``True``.
        :type keep_cross_validation_models: bool
        :param keep_cross_validation_predictions: Whether to keep the predictions of the cross-validation models.
               Defaults to ``False``.
        :type keep_cross_validation_predictions: bool
        :param keep_cross_validation_fold_assignment: Whether to keep the cross-validation fold assignment.
               Defaults to ``False``.
        :type keep_cross_validation_fold_assignment: bool
        :param fold_assignment: Cross-validation fold assignment scheme, if fold_column is not specified. The
               'Stratified' option will stratify the folds based on the response variable, for classification problems.
               Defaults to ``"auto"``.
        :type fold_assignment: Literal["auto", "random", "modulo", "stratified"]
        :param fold_column: Column with cross-validation fold index assignment per observation.
               Defaults to ``None``.
        :type fold_column: str, optional
        :param ignored_columns: Names of columns to ignore for training.
               Defaults to ``None``.
        :type ignored_columns: List[str], optional
        :param ignore_const_cols: Ignore constant columns.
               Defaults to ``True``.
        :type ignore_const_cols: bool
        :param score_each_iteration: Whether to score during each iteration of model training.
               Defaults to ``False``.
        :type score_each_iteration: bool
        :param k: The max. number of clusters. If estimate_k is disabled, the model will find k centroids, otherwise it
               will find up to k centroids.
               Defaults to ``1``.
        :type k: int
        :param estimate_k: Whether to estimate the number of clusters (<=k) iteratively and deterministically.
               Defaults to ``False``.
        :type estimate_k: bool
        :param user_points: This option allows you to specify a dataframe, where each row represents an initial cluster
               center. The user-specified points must have the same number of columns as the training observations. The
               number of rows must equal the number of clusters
               Defaults to ``None``.
        :type user_points: Union[None, str, H2OFrame], optional
        :param max_iterations: Maximum training iterations (if estimate_k is enabled, then this is for each inner Lloyds
               iteration)
               Defaults to ``10``.
        :type max_iterations: int
        :param standardize: Standardize columns before computing distances
               Defaults to ``True``.
        :type standardize: bool
        :param seed: RNG Seed
               Defaults to ``-1``.
        :type seed: int
        :param init: Initialization mode
               Defaults to ``"furthest"``.
        :type init: Literal["random", "plus_plus", "furthest", "user"]
        :param max_runtime_secs: Maximum allowed runtime in seconds for model training. Use 0 to disable.
               Defaults to ``0.0``.
        :type max_runtime_secs: float
        :param categorical_encoding: Encoding scheme for categorical features
               Defaults to ``"auto"``.
        :type categorical_encoding: Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder",
               "sort_by_response", "enum_limited"]
        :param export_checkpoints_dir: Automatically export generated models to this directory.
               Defaults to ``None``.
        :type export_checkpoints_dir: str, optional
        :param cluster_size_constraints: An array specifying the minimum number of points that should be in each
               cluster. The length of the constraints array has to be the same as the number of clusters.
               Defaults to ``None``.
        :type cluster_size_constraints: List[int], optional
        """
        super(H2OKMeansEstimator, self).__init__()
        self._parms = {}
        self._id = self._parms['model_id'] = model_id
        self.training_frame = training_frame
        self.validation_frame = validation_frame
        self.nfolds = nfolds
        self.keep_cross_validation_models = keep_cross_validation_models
        self.keep_cross_validation_predictions = keep_cross_validation_predictions
        self.keep_cross_validation_fold_assignment = keep_cross_validation_fold_assignment
        self.fold_assignment = fold_assignment
        self.fold_column = fold_column
        self.ignored_columns = ignored_columns
        self.ignore_const_cols = ignore_const_cols
        self.score_each_iteration = score_each_iteration
        self.k = k
        self.estimate_k = estimate_k
        self.user_points = user_points
        self.max_iterations = max_iterations
        self.standardize = standardize
        self.seed = seed
        self.init = init
        self.max_runtime_secs = max_runtime_secs
        self.categorical_encoding = categorical_encoding
        self.export_checkpoints_dir = export_checkpoints_dir
        self.cluster_size_constraints = cluster_size_constraints

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios=[.8], seed=1234)
        >>> pros_km = H2OKMeansEstimator(seed=1234)
        >>> pros_km.train(x=predictors,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')

    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios=[.8], seed=1234)
        >>> pros_km = H2OKMeansEstimator(seed=1234)
        >>> pros_km.train(x=predictors,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')

    @property
    def nfolds(self):
        """
        Number of folds for K-fold cross-validation (0 to disable or >= 2).

        Type: ``int``, defaults to ``0``.

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios=[.8], seed=1234)
        >>> benign_km = H2OKMeansEstimator(nfolds=5, seed=1234)
        >>> benign_km.train(x=predictors,
        ...                 training_frame=train,
        ...                 validation_frame=valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds

    @property
    def keep_cross_validation_models(self):
        """
        Whether to keep the cross-validation models.

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios=[.8], seed=1234)
        >>> ozone_km = H2OKMeansEstimator(keep_cross_validation_models=True,
        ...                               nfolds=5,
        ...                               seed=1234)
        >>> ozone_km.train(x=predictors,
        ...                training_frame=train,
        ...                validation_frame=valid)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_models")

    @keep_cross_validation_models.setter
    def keep_cross_validation_models(self, keep_cross_validation_models):
        assert_is_type(keep_cross_validation_models, None, bool)
        self._parms["keep_cross_validation_models"] = keep_cross_validation_models

    @property
    def keep_cross_validation_predictions(self):
        """
        Whether to keep the predictions of the cross-validation models.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios=[.8], seed=1234)
        >>> pros_km = H2OKMeansEstimator(keep_cross_validation_predictions=True,
        ...                              nfolds=5,
        ...                              seed=1234)
        >>> pros_km.train(x=predictors,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions

    @property
    def keep_cross_validation_fold_assignment(self):
        """
        Whether to keep the cross-validation fold assignment.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios=[.8], seed=1234)
        >>> ozone_km = H2OKMeansEstimator(keep_cross_validation_fold_assignment=True,
        ...                               nfolds=5,
        ...                               seed=1234)
        >>> ozone_km.train(x=predictors,
        ...                training_frame=train)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment

    @property
    def fold_assignment(self):
        """
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.

        Type: ``Literal["auto", "random", "modulo", "stratified"]``, defaults to ``"auto"``.

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios=[.8], seed=1234)
        >>> ozone_km = H2OKMeansEstimator(fold_assignment="Random",
        ...                               nfolds=5,
        ...                               seed=1234)
        >>> ozone_km.train(x=predictors,
        ...                training_frame=train,
        ...                validation_frame=valid)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment

    @property
    def fold_column(self):
        """
        Column with cross-validation fold index assignment per observation.

        Type: ``str``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> fold_numbers = cars.kfold_column(n_folds=5, seed=1234)
        >>> fold_numbers.set_names(["fold_numbers"])
        >>> cars = cars.cbind(fold_numbers)
        >>> print(cars['fold_numbers'])
        >>> cars_km = H2OKMeansEstimator(seed=1234)
        >>> cars_km.train(x=predictors,
        ...               training_frame=cars,
        ...               fold_column="fold_numbers")
        >>> cars_km.scoring_history()
        """
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column

    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns

    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars["const_1"] = 6
        >>> cars["const_2"] = 7
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_km = H2OKMeansEstimator(ignore_const_cols=True,
        ...                              seed=1234)
        >>> cars_km.train(x=predictors,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_km.scoring_history()
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols

    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios=[.8], seed=1234)
        >>> benign_km = H2OKMeansEstimator(score_each_iteration=True,
        ...                                seed=1234)
        >>> benign_km.train(x=predictors,
        ...                 training_frame=train,
        ...                 validation_frame=valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration

    @property
    def k(self):
        """
        The max. number of clusters. If estimate_k is disabled, the model will find k centroids, otherwise it will find
        up to k centroids.

        Type: ``int``, defaults to ``1``.

        :examples:

        >>> seeds = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/flow_examples/seeds_dataset.txt")
        >>> predictors = seeds.columns[0:7]
        >>> train, valid = seeds.split_frame(ratios=[.8], seed=1234)
        >>> seeds_km = H2OKMeansEstimator(k=3, seed=1234)
        >>> seeds_km.train(x=predictors,
        ...                training_frame=train,
        ...                validation_frame=valid)
        >>> seeds_km.scoring_history()
        """
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, int)
        self._parms["k"] = k

    @property
    def estimate_k(self):
        """
        Whether to estimate the number of clusters (<=k) iteratively and deterministically.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris['class'] = iris['class'].asfactor()
        >>> predictors = iris.columns[:-1]
        >>> train, valid = iris.split_frame(ratios=[.8], seed=1234)
        >>> iris_kmeans = H2OKMeansEstimator(k=10,
        ...                                  estimate_k=True,
        ...                                  standardize=False,
        ...                                  seed=1234)
        >>> iris_kmeans.train(x=predictors,
        ...                   training_frame=train,
        ...                   validation_frame=valid)
        >>> iris_kmeans.scoring_history()
        """
        return self._parms.get("estimate_k")

    @estimate_k.setter
    def estimate_k(self, estimate_k):
        assert_is_type(estimate_k, None, bool)
        self._parms["estimate_k"] = estimate_k

    @property
    def user_points(self):
        """
        This option allows you to specify a dataframe, where each row represents an initial cluster center. The user-
        specified points must have the same number of columns as the training observations. The number of rows must
        equal the number of clusters

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris['class'] = iris['class'].asfactor()
        >>> predictors = iris.columns[:-1]
        >>> train, valid = iris.split_frame(ratios=[.8], seed=1234)
        >>> point1 = [4.9,3.0,1.4,0.2]
        >>> point2 = [5.6,2.5,3.9,1.1]
        >>> point3 = [6.5,3.0,5.2,2.0]
        >>> points = h2o.H2OFrame([point1, point2, point3])
        >>> iris_km = H2OKMeansEstimator(k=3,
        ...                              user_points=points,
        ...                              seed=1234)
        >>> iris_km.train(x=predictors,
        ...               training_frame=iris,
        ...               validation_frame=valid)
        >>> iris_kmeans.tot_withinss(valid=True)
        """
        return self._parms.get("user_points")

    @user_points.setter
    def user_points(self, user_points):
        self._parms["user_points"] = H2OFrame._validate(user_points, 'user_points')

    @property
    def max_iterations(self):
        """
        Maximum training iterations (if estimate_k is enabled, then this is for each inner Lloyds iteration)

        Type: ``int``, defaults to ``10``.

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios=[.8], seed=1234)
        >>> benign_km = H2OKMeansEstimator(max_iterations=50)
        >>> benign_km.train(x=predictors,
        ...                 training_frame=train,
        ...                 validation_frame=valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations

    @property
    def standardize(self):
        """
        Standardize columns before computing distances

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> boston = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/BostonHousing.csv")
        >>> predictors = boston.columns[:-1]
        >>> boston['chas'] = boston['chas'].asfactor()
        >>> train, valid = boston.split_frame(ratios=[.8])
        >>> boston_km = H2OKMeansEstimator(standardize=True)
        >>> boston_km.train(x=predictors,
        ...                 training_frame=train,
        ...                 validation_frame=valid)
        >>> boston_km.scoring_history()
        """
        return self._parms.get("standardize")

    @standardize.setter
    def standardize(self, standardize):
        assert_is_type(standardize, None, bool)
        self._parms["standardize"] = standardize

    @property
    def seed(self):
        """
        RNG Seed

        Type: ``int``, defaults to ``-1``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS", "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios=[.8], seed=1234)
        >>> pros_w_seed = H2OKMeansEstimator(seed=1234)
        >>> pros_w_seed.train(x=predictors,
        ...                   training_frame=train,
        ...                   validation_frame=valid)
        >>> pros_wo_seed = H2OKMeansEstimator()
        >>> pros_wo_seed.train(x=predictors,
        ...                    training_frame=train,
        ...                    validation_frame=valid)
        >>> pros_w_seed.scoring_history()
        >>> pros_wo_seed.scoring_history()
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed

    @property
    def init(self):
        """
        Initialization mode

        Type: ``Literal["random", "plus_plus", "furthest", "user"]``, defaults to ``"furthest"``.

        :examples:

        >>> seeds = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/flow_examples/seeds_dataset.txt")
        >>> predictors = seeds.columns[0:7]
        >>> train, valid = seeds.split_frame(ratios=[.8], seed=1234)
        >>> seeds_km = H2OKMeansEstimator(k=3,
        ...                               init='Furthest',
        ...                               seed=1234)
        >>> seeds_km.train(x=predictors,
        ...                training_frame=train,
        ...                validation_frame= valid)
        >>> seeds_km.scoring_history()
        """
        return self._parms.get("init")

    @init.setter
    def init(self, init):
        assert_is_type(init, None, Enum("random", "plus_plus", "furthest", "user"))
        self._parms["init"] = init

    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios=[.8], seed=1234)
        >>> benign_km = H2OKMeansEstimator(max_runtime_secs=10,
        ...                                seed=1234)
        >>> benign_km.train(x=predictors,
        ...                 training_frame=train,
        ...                 validation_frame=valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs

    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        Type: ``Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder",
        "sort_by_response", "enum_limited"]``, defaults to ``"auto"``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS", "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios=[.8], seed=1234)
        >>> encoding = "one_hot_explicit"
        >>> pros_km = H2OKMeansEstimator(categorical_encoding=encoding,
        ...                              seed=1234)
        >>> pros_km.train(x=predictors,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding

    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> airlines = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip", destination_frame="air.hex")
        >>> predictors = ["DayofMonth", "DayOfWeek"]
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> air_km = H2OKMeansEstimator(export_checkpoints_dir=checkpoints_dir,
        ...                             seed=1234)
        >>> air_km.train(x=predictors, training_frame=airlines)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir

    @property
    def cluster_size_constraints(self):
        """
        An array specifying the minimum number of points that should be in each cluster. The length of the constraints
        array has to be the same as the number of clusters.

        Type: ``List[int]``.

        :examples:

        >>> iris_h2o = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris.csv")
        >>> k=3
        >>> start_points = h2o.H2OFrame(
        ...         [[4.9, 3.0, 1.4, 0.2],
        ...          [5.6, 2.5, 3.9, 1.1],
        ...          [6.5, 3.0, 5.2, 2.0]])
        >>> kmm = H2OKMeansEstimator(k=k,
        ...                          user_points=start_points,
        ...                          standardize=True,
        ...                          cluster_size_constraints=[2, 5, 8],
        ...                          score_each_iteration=True)
        >>> kmm.train(x=list(range(7)), training_frame=iris_h2o)
        >>> kmm.scoring_history()
        """
        return self._parms.get("cluster_size_constraints")

    @cluster_size_constraints.setter
    def cluster_size_constraints(self, cluster_size_constraints):
        assert_is_type(cluster_size_constraints, None, [int])
        self._parms["cluster_size_constraints"] = cluster_size_constraints


