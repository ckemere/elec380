Homework 3
##########

*This problem set is due Monday (10/24/2022) at midnight. Please turn in your
work by uploading to Canvas. If you have questions, please post them on the
course forum, rather than emailing the course staff. This will allow other
students with the same question to see the response and any ensuing discussion.
The goal of this problem set is to learn how to analyze spike trains.*

.. rst-class:: hwproblems

1. *Making a peristimulus time histogram*

    Refer to the Jupyter notebook (:download:`Homework3_Problem1.ipynb <Homework3_Problem1.ipynb>`).
    You will also need to download the data for the problem from (:download:`problem_1.npy <problem_1.npy>`).
    You can load it by::

        with open('problem_1.npy', 'rb') as loadfile:
            example_data = np.load(loadfile, allow_pickle=True) # Data for example below
            problem_data = np.load(loadfile, allow_pickle=True) # Data that you will use for your homework

    These (simulated) data correspond to the responses of two different neurons (:code:`example_data` and
    :code:`problem_data`) to a stimulus across 1000 trials of an experiment. For each neuron, there are spikes 
    recorded in 2 second windows, with the stimulus onset is at 0.25 s.

    **a.** In the PSTH shown in the example data, how long is the delay between when the stimulus appears
    (0.25 s) and the neuron begins to respond (it's firing rate differs from it's baseline)? We can
    define this as the "neural response latency".  Change the code to make the time bins wider 
    (decrease NumHistBins from 50 to 10). Now can you resolve the response latency with better or worse temporal resolution?
    Return the number of bins to 100, and change the code to calculate the PSTH for only the first 10 trials
    (change the line :code:`for trial in example_data:` to :code:`for trial in example_data[:10]:`).
    With this change, can you resolve the response latency with better or worse temporal resolution?

    **b.** Following the original example, make a perstimulus time histogram for the 1000 trials of the second
    neuron in the array `problem_data`. What is the response latency of this neuron? (You may change the value
    of NumHistBins to improve your estimation.) What is the maximum firing rate of this neuron during the period
    it is responding to the stimulus? What is it's baseline firing rate before the stimulus onset?

2. *Fano Factor and Response Variability*

    This `paper <https://www.nature.com/articles/nn.2501>`_ is a good reference on why the Fano Factor is interesting.
    Refer to the Jupyter notebook (:download:`Homework3_Problem2.ipynb <Homework3_Problem2.ipynb>`).
    You will also need to download the data for the problem from (:download:`problem_2.npy <problem_2.npy>`).
    You can load it by::

        with open('problem_2.npy', 'rb') as loadfile:
            example_data = np.load(loadfile, allow_pickle=True) # Data for example below
            problem_data = np.load(loadfile, allow_pickle=True) # Data that you will use for your homework

    These (simulated) data correspond to the responses of two different neurons (:code:`example_data` and
    :code:`problem_data`) to a stimulus across 1000 trials of an experiment. For each neuron, there are spikes 
    recorded in 2 second windows, with the stimulus onset is at 0.25 s.     
    
    **a.** Look at the Fano Factor plot in the notebook for the example neuron (:code:`example_data`). 
    Based on it's shape, do you think that there are any periods in which the response of the neuron is 
    more or less variable?

    **b.** Using the code in the notebook as an example, generate a Fano Factor plot for the second neuron
    (:code:`problem_data`). Based on it's shape, do you think that there are any periods in which the response 
    of the neuron is more or less variable?

    **c.** Now generate mean, variance, and Fano Factor plots for the first and
second halves of the second neuron's data (i.e., change :code:`problem_data` to
:code:`problem_data[:500]` for the first half or 
    :code:`problem_data[500:]` for the second half). Based on what you see, what do you think
    explains variability that you might have seen in **b.**?


3. *Calculating Tuning Curves*
 
    For this problem, we will use data which was archived on CRCNS.org. This data set contains the
    firing times of 10 neurons in cat visual cortex recorded during presentation of oriented drifting
    bars (`https://crcns.org/data-sets/vc/pvc-3/about <https://crcns.org/data-sets/vc/pvc-3/about>`_).
    Refer to the Jupyter notebook (:download:`Homework3_Problem3.ipynb <Homework3_Problem3.ipynb>`).
    You will also need to download the data for the problem from (:download:`problem_3.npy <problem_3.npy>`).
    You can load it by::

        with open('problem_3.npy', 'rb') as loadfile:
            stim_direction = np.load(loadfile, allow_pickle=True) # The stimulus direction for each trial in a 144 element vector
            spiketrains = np.load(loadfile, allow_pickle=True) # Raw data of spike times for each trial. Organized as a 10 element array (# of neurons) of 144 element arrays (# of trials) of numpy arrays (spike times)

    **a.** Fill in the missing code in order to calculate the tuning curves for the neurons. Which
    neuron has the highest firing rate for an orientation of the drifiting bar (it's "preferred orientation"). 
    What is it's maximum *firing rate* (in Hz- **NOTE: You need to think about both spike counts 
    and the duration of each trial!**)? Which neuron has the maximum firing rate for it's least-preferred orientation?
    Do you notice anything interesting about the structure of the tuning curves - is there usually one peak
    or two? Why do you think there might be more than one peak?

    **b.** When I examined the firing *times* on each trial, I noticed an interesting pattern. Calculuate
    the tuning curves for the neurons using either the first half of the response window or the second half.
    You can do this by changing how spike_counts is calculated - replace the line :code:`spike_counts[t,n] = len(trial)`
    with :code:`spike_counts[t,n] = sum(trial < 2)` for the first half or :code:`spike_counts[t,n] = sum(trial >=2)`
    for the second. What do you observe about the tuning curves? Why do you think that is?


