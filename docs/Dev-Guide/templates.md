Here are a few templates for various types of algorithms to provide a place to start developing your own readers, filters, writers, and sources!

## readers


## filters


## Writers

```py
# Import Helpers: TODO Check relativity
from ..base import WriterBase
from .. import _helpers

class WriteTemplate(WriterBase):
    def __init__(self):
        WriterBase.__init__(self, inputType='vtkPolyData')


    def RequestData(self, request, inInfoVec, outInfoVec):
        # Get the input data object
        pdi = self.GetInputData(inInfoVec, 0, 0)

        # TODO: Convert XXX data to YYY format

        # Write out
        with open(self.GetFileName(), 'w') as fout:
            # TODO: fill out
            fout.write('Data!\n')

        # Always return 1 from pipeline methods or seg-faults will occur
        return 1

```


## Sources
