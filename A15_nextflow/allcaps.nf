#!/usr/bin/env nextflow

params.str = "Hello World"

process convertToCaps {
    input:
    val inputString

    output:
    path 'output.txt'

    script:
    """
    echo "$inputString" | tr '[:lower:]' '[:upper:]' > output.txt
    """
}

workflow {
    convertToCaps(params.str)
}

