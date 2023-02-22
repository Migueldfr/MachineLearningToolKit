import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Union
import plotly.graph_objs as go
from plotly import subplots
from collections import defaultdict
import plotly.offline as py
from wordcloud import STOPWORDS
import plotly.express as px


def plot_multiclass_prediction_image(df, row_index: int, X_test: Union[pd.DataFrame, np.ndarray], prediction_col: str = 'Top Prediction', label_col: str = 'Label'):
    '''
    This will produce two plots side by side relating to a prediction of an image
    The first is the image titled with the label and the predicted label
    The second is a bar plot showing the actual probabilities of predictions for all classes

    Parameters
    ----------
    df : pd.DataFrame
        The dataset containing the results of the prediction along with the label and top predicted label
    row_index : int
        the index value for the image we want to plot
    X_test : pd.DataFrame or np.ndarray
        The X_test data
    prediction_col : str
        Defaults to 'Top Prediction' but should be the name of column with the prediction for image
    label_col : str
        Defaults to 'Label' but should be the name of column with the real label
    
    Return
    ----------
    displays plots

    '''

    to_plot = df.loc[[row_index]]

    fig, ax = plt.subplots(1, 2, figsize = (10, 5), constrained_layout = True)

    ax[0].imshow(X_test[row_index])
    ax[0].set_title(f'Label: {df.loc[row_index, prediction_col]}\nPrediction: {df.loc[row_index, label_col]}')

    df.loc[row_index, df.dtypes != object].plot.bar(ax = ax[1])
    plt.xticks(rotation = 45, ha = 'right')
    plt.title('Probabilities of Each Class')
    plt.show()



def plot_ngrams(df, target:str, text:str, n_gram:int):
    ''' 
    This function allows visualizing the frequency of occurrence of words and n-grams (sets of a number of consecutive words) based on the target variable.
    
    Parameters
    ----------
    - df: Dataframe with a text variable.
    - target: Column of the dataframe where the target variable is located.
    - text: Column of the dataframe where the text is located.
    - n_gram: Number of consecutive words whose frequency we want to visualize.
    
    Returns
    ----------
    - Bar chart representing the frequency of words, sorted from highest to lowest, divided by target variable.
    '''
    df1 = df[df[target] ==1]
    df0 = df[df[target] ==0]

    # Custom function for ngram generation 
    def generate_ngrams(text, n_gram):
        token = [token for token in text.lower().split(" ") if token != "" if token not in STOPWORDS]
        ngrams = zip(*[token[i:] for i in range(n_gram)])
        return [" ".join(ngram) for ngram in ngrams]

    # Custom function for horizontal bar chart 
    def horizontal_bar_chart(df, color):
        trace = go.Bar(
            y=df["word"].values[::-1],
            x=df["wordcount"].values[::-1],
            showlegend=False,
            orientation = 'h',
            marker=dict(
                color=color,
            ),
        )
        return trace

    # Get the bar chart from text with label 0 
    freq_dict = defaultdict(int)
    for sent in df0[text]:
        for word in generate_ngrams(sent, n_gram):
            freq_dict[word] += 1
    fd_sorted = pd.DataFrame(sorted(freq_dict.items(), key=lambda x: x[1])[::-1])
    fd_sorted.columns = ["word", "wordcount"]
    trace0 = horizontal_bar_chart(fd_sorted.head(50), 'blue')

    # Get the bar chart from text with label 1 
    freq_dict = defaultdict(int)
    for sent in df1[text]:
        for word in generate_ngrams(sent, n_gram):
            freq_dict[word] += 1
    fd_sorted = pd.DataFrame(sorted(freq_dict.items(), key=lambda x: x[1])[::-1])
    fd_sorted.columns = ["word", "wordcount"]
    trace1 = horizontal_bar_chart(fd_sorted.head(50), 'blue')

    # Creating two subplots
    fig = subplots.make_subplots(rows=1, cols=2, vertical_spacing=0.04,
                          subplot_titles=["Frequent words from text with label 0", 
                                          "Frequent words from text with label 1"])
    fig.add_trace(trace0, 1, 1)
    fig.add_trace(trace1, 1, 2)
    fig['layout'].update(height=1200, width=900, paper_bgcolor='rgb(233,233,233)', title="Word Count Plots")
    py.iplot(fig, filename='word-plots')

<<<<<<< HEAD
    return fig

=======
def sunburst(df, interior:str, exterior:str, col_num:str, title:str):
    '''
    This is a Plotly Graph similar to pie chart but with two levels, interior is for columns which have one or two unique values, and 
    the exterior is for columns which have more values.

    Parameters
	----------
    df -> dataframe we are working with 
    interior -> recommended for columns which have two or so uniques values. Must be 'str'
    exterior -> recommended for columns which have more values, because the graph has more space than inside. Must be 'str'
    col_num -> it,s the column which we want measured, show us the quantity of each value for both column (interior and exterior), must be 'str'
    title -> the title we want to show in the pie, must be 'str'

    Return
	----------

    Return a pie chart with two levels, interior and exterior.
    
    '''

    fig = go.Figure()
    fig = px.sunburst(df, path=[interior, exterior], values=col_num, template = 'plotly_dark')
    fig.update_layout(width=800, height=600, title = title)
    fig.show()

def wordcloudviz(column):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    """
    Function to create a quick visualization of wordclouds in a given column of a dataframe called df.

    Parameters
    ----------
    column = name of the column of the dataframe. 
             Input example: df['column_name']

    Return
    ---------
        A wordcloud visualization of the words in the column.
    """
    # First, it concatenates the text in a "single" text.
    text = " ".join(comment for comment in column)

    # Creates a wordcloud visualization
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
>>>>>>> 0f8d8abe7a26aac02e768b21b22a1d2e58bd6d30
