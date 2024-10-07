enum Source {
    CNN
    BBC
    REDDIT
    UNKNOWN
}

function IdentifySource(content: string) -> Source{
    /// Uses gpt-4o-mini to try and find the source of a block of content. Will ere on the safe side.
    client "openai/gpt-4o-mini"
    prompt #"
        Identify where this article is from.

        {{ctx.output_format}}

        If you are not sure, say UNKNOWN
        {{_.role('user')}}
        {{content}}
    "#
}