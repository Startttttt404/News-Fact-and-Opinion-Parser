A simple demonstration of Agentic AI principles, i.e. a system which delegates work to GenAI. A few things to note about these principles:

1.) Limit the outputs of the LLM to allow for a programmatic approach. I.e, using enums or json structures to ensure the LLM's output is consistent.
2.) Break down the task into the smallest task possible for the LLM. In this example, we took find the source, list of facts, and list of opinions and turned it into a bunch of seperate queries. First, determining the source, next going through each line and classifying it as a fact or opinion.
3.) Don't let the user interact with the LLM directly, give them a wrapper interface (I suppose the command line in this case, but it is a very simple example.)

To use the demo, you will need to provide the path to the file you want to parse (some tests are provided) and an OpenAI API key.