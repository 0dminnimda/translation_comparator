/* Python wrapper */
static PyObject *__pyx_pw_{num_fname}_1test(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_{num_fname}_1test = {"test", (PyCFunction)__pyx_pw_{num_fname}_1test, METH_NOARGS, 0};
static PyObject *__pyx_pw_{num_fname}_1test(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("test (wrapper)", 0);
  __pyx_r = __pyx_pf_{num_fname}_test(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_{num_fname}_test(CYTHON_UNUSED PyObject *__pyx_self) {
  int __pyx_v_p[1000];
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("test", 0);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_n_s_p); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 3, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);
/* … */
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_{num_fname}_1test, 0, __pyx_n_s_test, NULL, __pyx_n_s_{fname}, __pyx_d, ((PyObject *)__pyx_codeobj__2)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 3, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

====================================================================================================

-   (__pyx_v_p[0]) = 0x64;
  {
    Py_ssize_t __pyx_temp;
    for (__pyx_temp = 0; __pyx_temp < 0x3E8; __pyx_temp++) {
      __pyx_t_1[0+ (1 * __pyx_temp)] = 0;
    }
  }
  memcpy(&(__pyx_v_p[0]), __pyx_t_1, sizeof(__pyx_v_p[0]) * (1000));

