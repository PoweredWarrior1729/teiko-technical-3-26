# teiko-technical-3-26
An alleged take-home assignment for a job, assigned on 3-5-26.

# Running Code
To run, simply replace the cell-counts.csv file with your own data of the same format and name, or just use the one already there. Make sure you have python installed. Then, from the root directory of the repository, run the following commands in order.

`make setup`
`make pipeline`
`make dashboard`

## Link to Dashboard
http://localhost:8000

# Database Structure

Subject and sample ids are converted to integers for convenience. Otherwise, the data that is the same for each subject is placed into a Subjects table, whereas the data that differs between samples from the same subject are put into a Samples table, keyed by sample ids with references back to the subjects they came from.

This minimizes redudancy quite well, so the database will scale reasonably well for thousands more subjects and samples. However, there wasn't that much redundancy to begin with, so no the gains from this schema are relatively unimpressive as long as none of the strings in the database get too long.

With many different types of analysis to perform, we can query the database for any required data, since the storage format does not remove any of the data in the dataset, and SQL is flexible enough to perform any necessary query.

# Code Description

## Structure

Each step of the pipeline was placed into its own file in the `src` directory. There is a script to load the data, generate the summary table, create the box plots, and compute the results for the analysis in part 4. The one eexception to this modularity is that `load_data.py` is in the root directory as required, but even then it merely runs the code in the `src` directory that loads the code. Each step saves its results in the `assets` folder, which is accessed in order to display the results on the dashboard.

## Explanation

I designed the code in order to comply with the instructions and put as much code as possible into the `src` directory in order to keep the workspace clean and well organized. Each step was separated into its own python source file to keep the steps organized. The outputs had to be stored somewhere in order to be displayable entirely after running the pipeline, so the `assets` directory was created to hold that data for the dashboard. If I computed it when displaying the dashboard, the dashboard code could not be fully separated from the pipeline code, as the instructions seemed to suggest they should be.

# Results

No significant differences were found between the relative frequencies of cell types in responders and those of nonresponders, which is statistically justified by the overlap of the IQRs in the box plots. Every pair of box plots shows this overlap.
