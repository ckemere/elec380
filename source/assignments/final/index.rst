Final Project
##########

*The goal of the final project is for you to explore a few of the topics in the course in a bit of 
depth. You need to choose one of the three sub-assignments below. You may choose to do additional
problems as extra credit. Problems 1 and 2 are essay problems (~1000 words), and problem 3 involves 
coding. In addition to the references given, it is expected that you will cite at least 3 other papers. 
Make sure to cite your sources and include a reference section/bibliography at the end. Feel
free to include figures from sources that you cite or create your own.  You are 
welcome to propose an alternative topic/problem -- please do so before the end of classes.*

.. rst-class:: hwproblems


#. *Technologies for measuring the activity of all the neurons in the brain.*

    In class, we discussed a variety of techniques to measure the activity of neurons in the brain.
    Imagine that you've been given a nearly infinite budget by a philanthropist to embark on a
    ten year program to try to simultaneously record the activity of as many neurons in the brain of a mouse
    as possible. Would you fund electrode development, microscopy techniques, other approaches
    or all of the above? What are the benefits and limitations of each approach? What do you
    think is currently the biggest gap in our technologies in terms of measuring a specific part
    or fraction of the brain?

    References: 

    #. `<https://www.nature.com/articles/s41592-021-01257-6>`_
    #. `<https://iopscience.iop.org/article/10.1088/2515-7647/ac76f9/meta>`_
    #. `<https://www.nature.com/articles/s41551-022-00941-y>`_
    #. `<https://www.biorxiv.org/content/10.1101/2021.10.13.463862v1.abstract>`_
    #. `<https://www.science.org/doi/full/10.1126/science.abf4588>`_


#. *Artificial vision: the challenge of precisely controlling neural circuits*

    Imagine that you want to create a brain implant that will produce artificial vision.
    Specifically, assume that your goal is to precisely control the activity of individual
    neurons in primary visual cortex. Compare optogenetic solutions with solutions based on 
    electrodes. Questions that you likely want to address: What are the benefits and drawbacks 
    of each approach in terms of: 

    * controlling neural activity precisely, 
    * targeting the right neurons, 
    * logistically placing/controlling the interface (i.e., surgeries, implants, system size/weight), 
    * ethical concerns? 
    * other challenges


    
    References:

    #. `<https://www.nature.com/articles/s41593-021-00902-9>`_
    #. `<https://www.nature.com/articles/s41593-017-0018-8>`_
    #. `<https://www.sciencedirect.com/science/article/pii/S0896627320308072>`_
    #. `<https://iopscience.iop.org/article/10.1088/1741-2552/abd0ce/meta>`_
    #. `<https://www.science.org/doi/full/10.1126/science.abd7435>`_
    #. `<https://www.sciencedirect.com/science/article/pii/S0092867420304967>`_

#. *Decoding place cell activity*

    In class, we used Bayes rule to decode the choices of reaches. In this problem, you will use
    Bayes rule to decode the position of a rat in a maze. 

    In the references below, you'll see some example code that calculated place fields and
    decoded the position of a rat in 2D. For the final project, you need to do something similar.
    The data for the final project is found in the file :download:`final_project_data.nel <final_project_data.nel>`.
    This comprises the position data and spiking activity for a rat running in a linear track. Thus the
    position is 1-dimensional rather than 2-dimensional (as in the tutorial). 
    Example code showing how to load it is found in :download:`final_project_read_data.ipynb <final_project_read_data.ipynb>`
    Half way through the session, the maze was shortened, as described
    in this `paper <https://www.jneurosci.org/content/28/50/13448.short>`_. 
    Your task for the final project is to explore decoding this data. At minimum, you need to do the following:
    
    #. Following the tutorial in reference 2, use place cell activity to decode the animals position
    as they run through the maze. Note that the ratemap will be 1-dimensional (rate vs space) for this
    project rather than 2-dimensional, so if you want to calculate it using the helper functions, you'll
    need to use `TuningCurve1D` rather than `TuningCurve2D`. Run the whole process only on the first,
    long-track portion of the data.
    
    #. Modify the code so that you use the first K laps to estimate the ratemap rather than the entire
    long-track period. Calculate the decoding error for the subsequent laps. How does changing the value
    of K change the error? (Note that if you are following the tutorial, when you calculate the run
    epochs, laps will correspond to pairs of run epochs - one each for each direction on the track.)
    Plot the actual and decoded trajectories.

    #. Use the place field ratemap for the long track to decode the position on the short track. Compare
    this with what you get if you warp the position on the short track before calculating the error. 
    If the position data is in a `short_track_pos` nelpy object, you can warp it by doing:
        
        warped_short_track_pos = short_track_pos
        warped_short_track_pos.data = (warped_short_track_pos.data - offset) * scaling_factor

    where you've figured out by eye or by calculation what the `offset` and `scaling_factor`
    should be for the short track to span the same length as the long track.

    #. Optionally you can do more analyses (the effect of the number of neurons, the effect of different smoothing
    factors on decoding performance like in this paper `<https://onlinelibrary.wiley.com/doi/abs/10.1002/hipo.22714>`_, 
    etc.). If you are interested in doing replay analysis, please reach out and we can share the times of SWR
    with you.

    References:

    #. `<https://journals.physiology.org/doi/full/10.1152/jn.1998.79.2.1017>`_
    #. `<https://notebook.community/Summer-MIND/mind_2017/Tutorials/SpikeDecoding/spike_decoding_python>`_
