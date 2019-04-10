# UBC OcTree Mesh

Also see [Add Model](add-model.md)

## About this Reader
!!! failure "More to come!"
    There are a lot of pages in the documentation and we are trying to fill all content as soon as possible. Stay tuned for updates to this page

<!--- TODO --->

<iframe src="https://player.vimeo.com/video/281726394" width="640" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/281726394">PVGeo: UBC OcTree Reader</a> from <a href="https://vimeo.com/user82050125">Bane Sullivan</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

We tested this reader using the OcTree mesh found in [**this example**](http://giftoolscookbook.readthedocs.io/en/latest/content/AtoZ/DCIP/index.html) on the [**GIFtoolsCookbook website**](http://giftoolscookbook.readthedocs.io/en/latest/index.html):

- Mesh file: `CompleteTask/octree_mesh.txt`
- Model file: `CompleteTask/active_cells_topo.txt`

To use the plugin:

- Make sure to clone/update the *PVGeo* repo and [**install if you haven't already**](../../overview/getting-started.md)
- Select **File->Open...** in ParaView
- Choose the mesh file for your OcTree (we have enabled extensions: `.mesh` `.msh` `.dat` `.txt`)
- Select the **PVGeo: UBC OcTree Mesh File Format** reader when prompted.
- *Optional:* Click the **...** button next to the **File Name(s) Model** parameter field. You can select as many model files as you desire (each file will be appended as additional time steps for the same attribute defined by the **Data Name** parameter).
- Click **Apply** and wait... the load for larger OcTrees takes about 30 seconds.

!!! success "[Example Visualization](http://viewer.vtki.org/?fileURL=https://dl.dropbox.com/s/qybpnsn11lghnq9/OcTree.vtkjs?dl=0)"
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="http://viewer.vtki.org/?fileURL=https://dl.dropbox.com/s/qybpnsn11lghnq9/OcTree.vtkjs?dl=0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


!!! info "{lookup:PVGeo.ubc.octree.OcTreeReader}"

!!! info "{lookup:PVGeo.ubc.octree.OcTreeAppender}"
