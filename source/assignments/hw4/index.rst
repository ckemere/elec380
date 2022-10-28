Homework 4
##########

*This problem set is due Friday (11/04/2022) at midnight. Please turn in your
work by uploading to Canvas. If you have questions, please post them on the
course forum, rather than emailing the course staff. This will allow other
students with the same question to see the response and any ensuing discussion.
The goal of this problem set is to learn how to decode spike trains
by classification.*

.. rst-class:: hwproblems

For this homework, you'll need to download the data from the problems from
(:download:`homework4_spikes.npz <homework4_spikes.npz>` and 
:download:`homework4_metadata.npy <homework4_metadata.npy>`).

You can load it by::

    with open('homework4_spikes.npz', 'rb') as loadfile:
        spike_times = np.load(loadfile, allow_pickle=True)['spike_times']

    with open('homework4_metadata.npy', 'rb') as loadfile:
        metadata = np.load(loadfile)
        time_touch_held = metadata['time_touch_held'] # target onset times for each trial
        time_go_cue = metadata['time_go_cue'] # go cue time for each trial
        time_target_acquired = metadata['time_target_acquired'] # time the target was touched
        trial_reach_target = metadata['trial_reach_target'] # index of reach target for each trial (0 through 7)
            # note that I've "fixed" the reach targets to be 0-7 rather than 1-8
        target_locations = metadata['target_locations'] # x,y location of each target
        target_angles = metadata['target_angles'] # angle of each target


1. *Decoding Accuracy and the Plan Window*

    Refer to the Jupyter notebook (:download:`Homework4_Problem1.ipynb <Homework4_Problem1.ipynb>`).
    
    **a.** The first set of analyses that you will do is to quantify the effect of the duration of plan activity
    on performance. The example code calculates the decode accuracy for the shorter, 755 ms plan window
    trials. Run the notebook down to the cell that prints "Poisson Correct:" a few times and see that the performance 
    changes slightly. This is because we are randomly choosing training trials rather than selecting the first 25 in 
    each direction.
    Modify the code to use the first 750 ms of the plan window for both long and short trial
    types, by changing the line :code:`plan_spikes = extract_plan_spikes()`
    to :code:`plan_spikes = extract_plan_spikes(window_length=750)` to use the first 750 ms of plan activity
    for the spike counts for all trials, and changing the line
    :code:`target_trials = np.argwhere(short_trials & (trial_reach_target==c)).squeeze()` to be simply
    :code:`target_trials = np.argwhere((trial_reach_target==c)).squeeze()` (without the "short trials").
    Now we will have the same number of training trials but many more test trials. 
    Is the performance substantially different?

    **b.** Below the cell that prints "Poisson Correct:" is a skeleton for evaluating the performance
    as a function of the length of the plan window. Fill in the code as described in the comments. (You should
    be able to copy from the relevant cells above). When you run this cell and the following one, you
    should get a performance figure like the one saved in the notebook. Interpret the resulting figure -
    what duration of plan activity is required for reasonable performance?

    **c.** Now, set the length of the decode window to be 250 ms and try starting the plan period at
    different times by changing the line :code:`plan_spikes = extract_plan_spikes(window_length=plan_window)`
    to :code:`plan_spikes = extract_plan_spikes(window_length=250, start_offset=offset)`, where you
    change your loop to loop over an offset variable that you design to range from 0 to 500 (500 is
    the maximum offset that will fit for the 755 ms plan windows!). Interpret the result. Approximately
    when does the most useful movement-planning related neural activity begin to be expressed?

2. *How does performance depend on the number of neurons available?*

    **a.** Modify the code from Problem 1 to choose a random subset of neurons to use for decoding. 
    Using a 250 ms duration plan window starting after a 100 ms ofset, evaluate average decoding
    performance as a function of the number of neurons used by the decoder. Specifically, repeatedly
    (at least 25 times) randomly sample groups of neurons of size 30, 60, 90, 120, and 150, and calculate 
    average decode performance. About how many neurons do  you need for good performance?

    **Hints on code to modify.** If the indices of your random neurons are in :code:`neuron_idx`, you
    need to change the code that calculates the mean spike counts:

        num_neurons = len(neuron_idx)
        mean_spike_counts = np.zeros((num_neurons, 8))
        for c in range(8):
            mean_spike_counts[:,c] = np.mean(plan_spikes[training_trials[c], neuron_idx], axis=0)

    Furthemore, you'll need to change the code that calculates the likelihood:

            poisson_likelihood[:,c] = \
                multivariate_poisson_logpdf(m, plan_spikes[test_trials, neuron_idx])

    To get random indices of neurons, you can use the :code:`numpy.random.choice` function.

        np.random.choice(range(190), NUMBER_OF_NEURONS, replace=False)

    In particular, the "replace=False" instruction is important. Without it, the default
    is to potentially give multiple copies of the same value.

    **b.** If you choose the 30 neurons with the highest average firing rates or the 30 neurons
    with the lowest average firing rates, how does their decode performance compare with
    average performance from randomly selected neurons?

    **Extra Credit.** What is the minimum size of ensemble that will yield good performance? (Canvas
    you cherry-pick the best neurons?)


3. *How does performance depend on the quantity of training data?*
 
    Modify the notebook from problem 1 to test the effect of changing the size of the
    training data set using a 250 ms duration plan window starting after a 100 ms ofset. 
    How does decode performane compare for training sets of size 5, 10, 15, 20, 25, 30, 35, 
    and 40?

