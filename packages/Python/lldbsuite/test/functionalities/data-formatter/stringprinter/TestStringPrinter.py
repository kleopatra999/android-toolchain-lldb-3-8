import lldbsuite.test.lldbinline as lldbinline
import lldbsuite.test.lldbtest as lldbtest

lldbinline.MakeInlineTest(__file__, globals(), [lldbtest.expectedFailureWindows("llvm.org/pr24772")])
