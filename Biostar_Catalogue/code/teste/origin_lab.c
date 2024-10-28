// Create Matrix Page and Send Data to It
static void Main(string[] args)
{
    Origin.Application oApp = new Origin.Application();
    oApp.NewProject();
    double[,] data = new double[100, 100];
    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++)
            data[i, j] = i * j;

    // Create Matrix Page
    string mpname = oApp.CreatePage((int)Origin.PAGETYPES.OPT_MATRIX);
    Origin.MatrixPage mp = oApp.FindMatrixSheet(mpname).Parent;

    // Number of Matrix Sheets: 3
    while (mp.Layers.Count < 3)
        mp.Layers.Add();

    foreach (Origin.MatrixSheet msht in mp.Layers)
    {
        msht.Name = "MSheet" + msht.Index.ToString();

        // Number of Matrix Object per Matrix Sheet: 4
        msht.Mats = 4;

        // Dimension: 100x100
        msht.Cols = 100;
        msht.Rows = 100;

        // Send Data to Matrix Object
        foreach (Origin.MatrixObject mo in msht.MatrixObjects)
            mo.SetData(data);
    }

    oApp.Save(System.IO.Directory.GetCurrentDirectory() + @"\MatrixPage.opj");
    oApp.Exit();
}