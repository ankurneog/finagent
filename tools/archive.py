import os
from datetime import datetime
class ArchiveManager():
    def __init__(self, args):
        self.ticker = args.symbol.lower()
        self.archive_path = os.path.join(args.output_dir, self.ticker)
        os.makedirs(self.archive_path, exist_ok=True)
    def save_df(self, df, filename: str):
        """
        Saves a DataFrame to a CSV file in the archive directory.
        
        :param df: DataFrame to save.
        :param filename: Name of the file to save the DataFrame as.
        """
        date_str = datetime.now().strftime("%Y%m%d")
        file_path = os.path.join(self.archive_path, f"{self.ticker}_{date_str}_{filename}.csv")
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    
    def save_plot(self, plot, filename: str):
        """
        Saves a plot to the archive directory.
        
        :param plot: Plot object to save.
        :param filename: Name of the file to save the plot as.
        """
        file_path = os.path.join(self.archive_path, filename)
        plot.savefig(file_path)
        print(f"Plot saved to {file_path}")
    
    def save_commentary(self, commentary: str):
        """
        Saves a commentary to a text file in the archive directory.
        
        :param commentary: Commentary text to save.
        :param filename: Name of the file to save the commentary as.
        """
        date_str = datetime.now().strftime("%Y%m%d")
        file_path = os.path.join(self.archive_path, f"{self.ticker}_{date_str}_commentary.txt")
        with open(file_path, 'a') as f:
            f.write(commentary + '\n')
        print(f"Commentary saved to {file_path}")
    
    