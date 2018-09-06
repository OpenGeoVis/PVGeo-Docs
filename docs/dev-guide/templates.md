Here are a few templates for various types of algorithms to provide a place to start developing your own readers, filters, writers, and sources!

## Readers


## Filters


## Writers

```py
# Import Helpers: TODO Check relativity
from ..base import WriterBase
from .. import _helpers

class WriteTemplate(WriterBase):
    """A writer template for you! Write the overall description of this writer
    here. E.g. This writers takes ``XXX`` as and saves it to a file of the
    ``YYY`` format for use in software such as ZZZ.
    """
    __displayname__ = 'Write Template'
    __category__ = 'writer'
    def __init__(self, **kwargs):
        WriterBase.__init__(self, inputType='vtkDataSet', **kwargs)
        # Set private variables here!
        self.__foo = kwargs.get('foo', True)


    def PerformWriteOut(self, inputDataObject, filename):
        """Use ``inputDataObject`` and ``filename`` to save the VTK data object
        to your custom file type.

        Args:
            inputDataObject (vtkDataObject): This is guaranteed to be of the type specified by the ``inputType`` in your ``__init__`` unless you override ``FillInputPortInformation``.
            filename (str): A full filename with an index appended if needed. Use this string to save your data.

        Return:
        int: return 1 on success
        """
        raise NotImplementedError('Code me up!')
        # Always return 1
        return 1

    def SetFoo(self, foo):
        """Set the foo variable"""
        if self.__foo != foo:
            self.__foo = foo
            self.Modified()

```


## Sources

```py
# Import Helpers: TODO: Check relativity
from ..base import AlgorithmBase
from .. import _helpers

class TemplateSource(AlgorithmBase):
    """A source template for you! Write the overall description of this source
    here. E.g. This source produces a ``XXX`` object that describes some
    useful information.
    """
    __displayname__ = 'Template Source'
    __category__ = 'source'
    def __init__(self, **kwargs):
        AlgorithmBase.__init__(self,
            nInputPorts=0,
            nOutputPorts=1, outputType='vtkPolyData')
        # Set private variables here!
        self.__foo = kwargs.get('foo', True)

    def RequestData(self, request, inInfo, outInfo):
        """This is where you fill out your algorithm"""
        pdo = self.GetOutputData(outInfo, 0)
        # TODO: Fill in the output data object: ``pdo``
        raise NotImplementedError('Code me up!')
        return 1

    def SetFoo(self, foo):
        """Set the foo variable"""
        if self.__foo != foo:
            self.__foo = foo
            self.Modified()

```
