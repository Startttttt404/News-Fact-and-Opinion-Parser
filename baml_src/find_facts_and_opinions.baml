enum ContentType{
    FACT
    OPINION
}

function IdentifyContentType(content: string) -> ContentType{
    /// Uses gpt-4o-mini to decide if a string is a fact or opinion.
    client "openai/gpt-4o-mini"
    prompt #"
        Indentify if this is a fact or opinion.

        {{ctx.output_format}}

        {{_.role('user')}}
        {{content}}
    "#
}

