path: tree/master/snippets
source: PV_Composite_Writer.py

# Composite Data Writers

!!! info "Author"
    This snippet was written by [**Bane Sullivan**](http://banesullivan.com) and was originally posted on ParaView's GitLab project snippets [**here**](https://gitlab.kitware.com/paraview/paraview/snippets/425).

    See the [**source**](#__source) section for the resulting output.

The functionality using decorated `VTKPythonAlgorithmBase` classes as ParaView
plugins has a composite support option for the `smdomain` input property that is
incredibly simple to use with filter algorithms yet can be tricky to use for
writer algorithms.

```py hl_lines="3"
@smproxy.writer(...)
@smproperty.input(name="TableInput", port_index=0)
@smdomain.datatype(dataTypes=["vtkTable"], composite_data_supported=True)
class MyWriter(VTKPythonAlgorithmBase):
       ...
```

The provided snippet in the [**source**](#__source) section of this page
provides a simple base class for a user to inherit functionality which is a
modification of PVGeo’s `WriterBase` algorithm ({lookup:PVGeo.base.WriterBase}).
In this example I demonstrate the use of this base class through creating a
writer algorithm that will save out XYZ+attribute data of the cell centers and
cell data for any given input datasets. This solution handles altering the given
filename to save out each object in the composite dataset separately by saving
each block out in `PerformWriteOut`  method that is repeatedly called by
`RequestData` explicitly.

!!! note
    Note that we must use the `composite_data_supported=True` flag for the `@smproxy.writer(...)` declaration as well as append allowable input types within the algorithms `FillInputPortInformation` method.



```py hl_lines="5 14 17 18 19 20"
# This is partially pseudo-code and is implemented in `WriterBase`

@smproxy.writer(...)
@smproperty.input(name="Input", port_index=0)
@smdomain.datatype(dataTypes=["vtkDataSet"], composite_data_supported=True)
class MyWriter(VTKPythonAlgorithmBase):
       ...

    def FillInputPortInformation(self, port, info):
        """Allows us to save composite datasets as well.
        NOTE: I only care about ``vtkMultiBlockDataSet``s
        """
        info.Set(self.INPUT_REQUIRED_DATA_TYPE(), self.InputType)
        info.Append(self.INPUT_REQUIRED_DATA_TYPE(), 'vtkMultiBlockDataSet')
        return 1

    def PerformWriteOut(self, inputDataObject, filename):
        """This method must be implemented. This is automatically called by
        ``RequestData`` for single inputs or composite inputs."""
        raise NotImplementedError('PerformWriteOut must be implemented!')

    def RequestData(self, request, inInfoVec, outInfoVec):
        """Subclasses must implement a ``PerformWriteOut`` method that takes an
        input data object and a filename. This method will automatically handle
        composite data sets.
        """
        inp = self.GetInputData(inInfoVec, 0, 0)
        # Handle composite datasets.
        # NOTE: This only handles 'vtkMultiBlockDataSet'
        if isinstance(inp, vtk.vtkMultiBlockDataSet):
            num = inp.GetNumberOfBlocks()
            # Create a list of filenames that vary by block index
            self.SetBlockFileNames(num)
            for i in range(num):
                data = inp.GetBlock(i)
                if data.IsTypeOf(self.InputType):
                    self.PerformWriteOut(data, self.GetBlockFileName(i))
                else:
                    print('Invalid input block %d of type(%s)' % (i, type(data)))
        # Handle single input dataset
        else:
            self.PerformWriteOut(inp, self.GetFileName())
        return 1

```
